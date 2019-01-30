# 12_SNS

## 1.開始之前
- 在SNS Console點選 Get started
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548649782336_1.jpg)

## 2.建立主題

(1) Create new topic

- Topic name(主題名稱):cc104_sns
- Display name:cc104_sns
- 設定好後，點選Create topic
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548654833072_sns2.jpg)


(2)創建好Topic後，可看到Topic Detail(主題詳細資訊)的頁面

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548654841711_sns3.jpg)

## 3.建立訂閱

(1)先點選Create subscription(建立訂閱)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548655594233_sns4.jpg)


(2)Create subscription

- Topic ARN: 剛剛建立之Topic(cc104_sns)的ARN會直接顯示在該欄位
- Protocol: 通訊協定選擇Email
- Endpoint: 端點欄位輸入Email
- 以上都設定完成後，點選Create subscription
![](https://d2mxuefqeaa7sj.cloudfront.net/s_3BCFEA1BC1CD72391D1DCA4B014C44C6EC9A56418E897492249F9096487FE47D_1548742010999_sns1.jpg)


(3)到郵件信箱去接受驗證信

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548660552969_999.jpg)


(4)點選驗證後，出現之頁面(認證成功)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_3BCFEA1BC1CD72391D1DCA4B014C44C6EC9A56418E897492249F9096487FE47D_1548741998356_sns6.jpg)

## 4.發佈到主題(Publish to topic)

發佈者傳送訊息到該主題。
一旦發佈新訊息時，SNS會嘗試傳遞該訊息給每個已經訂閱該主題的端點(在這裡指我們剛才在前項作業指定的Email)
(1)在剛剛創建的主題(cc104_sns)的頁面中，點選Publish to topics

![](https://d2mxuefqeaa7sj.cloudfront.net/s_3BCFEA1BC1CD72391D1DCA4B014C44C6EC9A56418E897492249F9096487FE47D_1548741953788_sns5.jpg)


(2)Publish a Message

- Topic ARN : 前項作業創建之Topic(cc104_sns)的ARN
- Subject(主題): cc014_sns_test
- Message format(訊息格式) :JSON
- 點選 JSON message generator(見下圖)
  - Message:This is a test message from cc104
  - Target platforms: 這裡指選擇Email
  - 前兩項設定好後，點選Generate JSON(把你在Message輸入的內容轉換成JSON格式)
- 可發現在Message欄位中，出現以JSON格式呈現的訊息內容
- 上述設定都完成後，點選Publish message(發佈訊息)


![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548657871049_12.jpg)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548657858063_11.jpg)


(3)發佈訊息後，可至端點查看是否接受到訊息

- 到前面作業中設定之端點Email中確實接收到訂閱的主題傳來的訊息
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548657884304_13.jpg)

## 5.取消訂閱主題

(1)選擇左邊窗格中的Subscription
(2)勾選訂閱清單中想要取消的訂閱
(3)點選上方Actions中的Delete subscriptions

![](https://d2mxuefqeaa7sj.cloudfront.net/s_3BCFEA1BC1CD72391D1DCA4B014C44C6EC9A56418E897492249F9096487FE47D_1548741794614_sns2.jpg)


(4)點選Delete

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548659009531_32.jpg)


(4)成功刪除訂閱後會短暫出現Subscription deleted的通知

![](https://d2mxuefqeaa7sj.cloudfront.net/s_3BCFEA1BC1CD72391D1DCA4B014C44C6EC9A56418E897492249F9096487FE47D_1548741874018_sns4.jpg)



## 6.刪除主題

刪除一個主題的同時，同時也會刪除所有在該主題的訂閱
(1)選擇左邊窗格中的Topics
(2)勾選要刪除的主題
(3)點選上方Actions中的Delete topics


![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548659020150_34.jpg)


(4)點選Delete

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548659193115_image.png)


(5)成功刪除主題後，會短暫出現Topics deleted的通知，此時發現原先的主題已不在畫面上

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CF056E35B54101733906EB8D89D2F9B899D4134D6DB5B4F08E57A7E5EE9FCB84_1548659209990_42.jpg)



