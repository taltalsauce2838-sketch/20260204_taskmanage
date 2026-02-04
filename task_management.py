# 20260204課題 :タスク管理のCLIアプリ(DB連携)になります。
import sys
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="mysql",
    db="TaskManage",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

#タスクをDBに追加するオブジェクト
def task_add(uid,name,detail,deadline):
    with conn.cursor() as cursor :
        sql = """INSERT INTO tasks (uid, name, detail, deadline) value (%s, %s, %s, %s)"""
        cursor.execute(sql,(uid,name,detail,deadline))
    conn.commit()

#タスク一覧をDBから表示するオブジェクト
def task_list(comp):
    #"-c"オプションをつけた場合完了(statusが"Complete"もしくは"完了")のタスクを除いて表示
    if comp == "-c" :
        with conn.cursor() as cursor :
            sql = """SELECT t.*, u.name FROM tasks t LEFT JOIN users u ON t.uid = u.id WHERE UPPER(status) NOT IN ('COMPLETE', '完了') """
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows :
                print(row)
        conn.commit()
    #それ以外の場合はすべてのタスクを表示
    else :
        with conn.cursor() as cursor :
            sql = """SELECT t.*, u.name FROM tasks t LEFT JOIN users u ON t.uid = u.id """
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows :
                print(row)
        conn.commit()

#タスクをDBから更新するオブジェクト
def task_update(id,column,value):
    with conn.cursor() as cursor :
        sql = f"UPDATE tasks SET {column} = %s WHERE id = %s"
        cursor.execute(sql,(value,id))
    conn.commit()
#
# タスクをDBから削除するオブジェクト
def task_delete(id):
    with conn.cursor() as cursor :
        sql = """DELETE FROM tasks WHERE id = %s"""
        cursor.execute(sql,(id,))
    conn.commit()

#アプリケーション本体
def main(args):
    print(args)
    # mysql接続


    #第一引数で機能を分岐、指定引数は[add/list/update/delete]とする。
    #タスク新規追加機能
    if args == "add" :
        print("addコマンド分岐")
        uid = input("uidを入力してください: ").strip()
        name = input("タスク名を入力してください: ").strip()
        detail = input("タスク詳細を入力してください: ").strip()
        deadline = input("期限を入力してください(YYYY/MM/DD): ").strip()
        task_add(uid,name,detail,deadline)

    #タスク一覧表示機能
    elif args == "list" :
        print("listコマンド分岐")
        if len(sys.argv) >= 3:
            task_list(sys.argv[2])
        else :
            task_list(0)

    #タスク情報更新機能
    elif args == "update" :
        print("updateコマンド分岐")
        id = input("更新したいタスクidを入力してください: ").strip()
        column = input("更新したいデータ種別を入力してください: ").strip()
        if column == "uid" or column == "name" or column == "detail" or column == "deadline" or column == "status":
            pass
        else :
            print("指定されたデータ種別は存在していません。uid/name/detail/deadline/statusの何れかを入力してください。")
            sys.exit()
        value = input("更新したいデータの内容を入力してください: ").strip()
        task_update(id,column,value)

    #タスク情報削除機能
    elif args == "delete" :
        print("deleteコマンド分岐")
        id = input("削除したいタスクidを入力してください: ").strip()
        task_delete(id)

    elif args == "non" :
        print("引数なし分岐")
        print("引数はadd/list/update/deleteの何れかを指定してください。")

    else :
        print("その他不正な引数などの分岐")
        print("引数はadd/list/update/deleteの何れかを指定してください。")

    conn.close()

# アプリ開始地点指定
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main("non")
    else:
        main(sys.argv[1])