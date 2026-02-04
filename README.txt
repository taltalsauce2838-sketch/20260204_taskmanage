##ファイル名：
　task_management.py

##ツール概要；
　タスク一覧へのタスクの追加/リスト表示/更新/削除をCLIで行うお試しアプリケーション

##動作バージョン：
　Python 3.13.9
　mysql 5.7.44-log

##操作コマンド
　python3 task_management.py [add/list (-c)/update/delete]
　第一引数に操作種別を入力することで以下のようにコマンドを分岐
　add		：タスクの新規追加、モード選択後応答形式でuid(ユーザID),name(タスク名),detail(タスク詳細),deadline(タスク期限)を入力して登録を実施。
　list		：登録されているタスクの一覧を表示、第二引数に"-c"を指定した場合statusが完了ではないタスク一覧を表示する。
　update	：登録されているタスクの更新、id(更新対象のタスクID),column(更新したいカラム),value(更新データ)を入力して更新を実施。
　            変更可能パラメータはuid(ユーザID)/name(タスク名)/detail(タスク詳細)/deadline(タスク期限)/status(タスク状態)としている。
　detele	：登録されているタスクの削除、id(更新対象のタスクID)を入力して削除を実施。

