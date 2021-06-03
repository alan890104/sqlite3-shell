# Sqlite3 Shell
command windows to 


|指令|說明|  
|----|----|  
|ls|顯示所有列表名稱與表頭|  
|help|顯示所有指令|  
|<任何sql語法>|執行sql指令|  
|exit|離開程式(也可雙擊Enter)|  

## installation
### 1. GOTO [Github Release](https://github.com/alan890104/sqlite3-shell/releases/latest) and click db_shell.exe   
![Github Release and download](https://i.imgur.com/Gokq0ZT.png)

### 2. Double Click db_shell.exe will pop up a message box, click "Other Information"(其他資訊)   
![](https://i.imgur.com/cwE0MPc.png)
### 3. Click this button(仍要執行) and you are able to use this shell!   
![](https://i.imgur.com/bIHXD6J.png)

## Example
```sql=
-- create a table and insert
CREATE TABLE user(name PRIMARY KEY,age NOT NULL);
INSERT INTO user VALUES("Alan",21);
INSERT INTO user VALUES("Yoyo",15);
INSERT INTO user VALUES("David",24);
```
![](https://i.imgur.com/jLSqgLx.png)
----------------------------------
```sql=
-- show all of your tables
ls
```
![scene](https://i.imgur.com/1xEqAFr.png)