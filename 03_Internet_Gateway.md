# 03_Internet Gateway

## 1.先點選左方Internet Gateways，再點選Create Internet gateway
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548585424542_41.jpg)

## 2.Create Internet gateway
- Name tag: cc104_igw
- 設定完成後，點選右下角Create
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548585431309_42.jpg)

## 3.創建完成後出現該頁面，再按Close
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548585435821_43.jpg)

## 4.Internet Gateways出現剛才創建完成的cc104_igw
- **但state狀態是detached**，沒有attach
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548585496892_44.jpg)

## 5.點選cc104_igw後，選擇Actions中的Attach to VPC
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548590561167_91.jpg)

## 6.在Attach to VPC中，選擇之前創建好的cc104_vpc後，點選右下角”Attach”
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548590739199_92.jpg)

## 7.可看到IGW已經attach到VPC
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548728268109_4.jpg)



