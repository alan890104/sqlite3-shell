# Sqlite3 Shell
A prettify command window to display sqlite3 interface.


|指令|說明|  
|----|----|  
|ls|顯示所有列表名稱與表頭|  
|help|顯示所有指令|  
|<任何sql語法>|執行sql指令|  
|exit|離開程式(也可雙擊Enter)|  

|instructions|explain|  
|----|----|  
|ls|show schemas of tables|  
|help|show all instructions|  
|<sql_command>|execute sql command|  
|exit|exit program(or double click Enter)|  

## installation
### 1. Goto [Github Release](https://github.com/alan890104/sqlite3-shell/releases/latest) and click db_shell.exe   
![Github Release and download](https://i.imgur.com/Gokq0ZT.png)

### 2. Double click db_shell.exe and it will pop up a message box. Select "Other Information".(其他資訊)   
![](https://i.imgur.com/cwE0MPc.png)
### 3. Click this button(仍要執行) and you are able to use this shell!   
![](https://i.imgur.com/bIHXD6J.png)
### 4. You can named for your database or press ENTER to use default name(DB.sqlite3).   
![](https://i.imgur.com/LZhqXHV.png)
### 5. Type some sql command!!
::: danger
You should type a semicolon ";" at the end of the sql command. 
:::
![](https://i.imgur.com/HnBtKDw.png)

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

###### tags: `python` `sql` `sql shell` `sqlite3`