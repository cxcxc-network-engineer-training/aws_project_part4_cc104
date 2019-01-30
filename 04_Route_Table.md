# 04_Route Table

# 創建公網段路由表
- 當您建立 VPC 時，便會自動隨附一個主路由表(Main Route Table)，且該Main RT會自動與此VPC中的Subnet關聯。因此，這裡我們只需再自創一個預設之外的路由表並將其關聯至Subnet即可。
## 1.先點選左方Route Tables，再選上方的Create route table
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548586782408_51.jpg)

## 2.創建Route Table
- Name tag: cc104_public_rt 
- VPC:選擇之前創建好的cc104_vpc
- 設定好後，點選Create
![](https://d2mxuefqeaa7sj.cloudfront.net/s_9E3F718E84A3608B99BAD50C112B49EDF0DF87D510155714CC8B6962BEEF3AFA_1548586845246_52.jpg)



## 3.確認創建好的Route Table有出現在畫面中
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548664756787_1.jpg)

## 4.對公網段路由表做設定

(1) 先點選cc014_public_rt
(2) 再點選下方Routes
(3) 接著點選Edit routes (編輯路由表)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548643067982_1.jpg)


**4-1.公網段-Edit routes**
(1)先點選**Add route**
(2)Destination輸入 **0.0.0.0/0**
(3)Target選擇**Internet Gateway**

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548643079990_2.jpg)


(4)點選之前創建好的Internet Gateway(cc104_igw)
(5)點選Save routes，以儲存設定好的路由

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548643874530_3.jpg)


(6)看到路由成功設定後的畫面，點選Close

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548643906381_4.jpg)


(7)確認剛剛新增的路由0.0.0.0/0有出現在公網段路由中

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548643925737_5.jpg)


**4-2.把公網段的路由表，與Subnet做連結**
(1) 在cc104_public_rt中，先點選Subnet Associations，再點選Edit subnet associations

- 先選擇公網段路由表(cc104_public_rt)
- 點選Subnet Associations
- 點選Edit subnet associations
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548648435582_43.jpg)


(2) 編輯子網段連結

- 先點選之前創建好的子網段(cc104_web_subnet)
- 再點選Save
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548645005526_12.jpg)


(3)設定好連結後，可在公網段路由表中的Subnet Associations看到它已經與子網段(cc014_web_subnet)連結

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548645012181_13.jpg)


