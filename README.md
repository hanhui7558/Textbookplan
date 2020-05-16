# Textbookplan
教材填报系系统，用户登录，根据用户单位，显示该单位的教学任务
设置了三个model：account/MyUser 增加了 unit(用户单位)属性；index/TeachingTask：教学任务，textbookorder/BookOrder：教材计划
业务逻辑：为每个单位分配一个账号，登录账号根据单位，显示该单位下的教学任务，根据教学任务填写教材信息，一对一的关系。
遇到问题，a.根据用户单位筛选该单位下的教学任务数据，在前台呈现; b.用户填写教材计划以后，数据传到数据库，并在bklist页面展示教材计划信息，并导出excle表格文件。
