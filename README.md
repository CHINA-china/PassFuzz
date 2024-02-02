# PassFuzz
一款适用于渗透测试、红队、src挖掘的弱口令生成工具

密码组合规律是来自多个项目里获取到的一些密码，经过分析后，总结出来的常见规律

脚本会自动对输出结果进行排序，将首字母大写、全小写的组合优先放前面

生成的结果样例见Demo文件夹内
## user
生成针对于员工、用户密码的字典，输出文件名：UserPass.txt
```
脚本会对name.txt中每个单词进行首字母大写、全缩写转换后按以下规律组合
组合规律：
name.txt + year.txt
name.txt + year.txt + symbol.txt
name.txt + 日期
name.txt + 日期 + symbol.txt
name.txt + 常规弱口令
name.txt + 常规弱口令 + symbol.txt
```
## system
生成针对于系统管理员密码的字典，输出文件名：Max.txt、Mini.txt
```
MaxFuzz.py脚本会遍历name.txt中每个单词的字母进行大小写组合，之后按以下规律组合，此脚本生成的密码量较多，覆盖广，但是爆破流量也大。
MiniFuzz.py脚本只对name.txt中每个单词进行首字母大写、全缩写转换，之后按以下规律组合，此脚本生成的密码更精简，并且组合规律更为常见，推荐优先使用。
组合规律：
name.txt + num.txt
name.txt + symbol.txt + num.txt
```
