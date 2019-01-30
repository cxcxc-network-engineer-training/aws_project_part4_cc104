# 07_ELB

## 1.開始之前，先點選進入EC2 Console
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548747841475_elb3.jpg)

## 2.Select load balancer type :選擇Classic Load Balancer
- Classic Load Balancer 提供跨多個 Amazon EC2 執行個體的基本負載平衡功能，而且可同時在請求層與連線層運作
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548748277856_classic.jpg)

## 3.先點選左邊窗格中的Load Balancers，再點選Create Load Balancer
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548747691446_elb1.jpg)

## 4. Define Load Balancer(Step1)
- Load Balancer Name：cc104-elb
- Create LB Inside：選擇之前創建好的cc104_vpc
- Listener Configuration(建立負載平衡器的接聽程式): HTTP 80port
- Select Subnets：從Available subnets(可用的子網段)中選取cc104_web_subnet(10.10.1.0/24)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548588613257_Snipaste_2019-01-27_19-16-47.png)

## 5.Assign Security Groups(Step2)

(1) Select an existing security group (選擇現有的防火牆)
(2)點選Next Configure Security Settings

![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548748038568_Snipaste_2019-01-28_10-11-47.png)

## 6.Configure Security Settings(Step3)
- 點選 Next Configure Health Check
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548748214244_123.png)

## 7.Configure Health Check(Step4)

(設定負載平衡器的運作狀態檢查)
(1)Ping Protocol : 選擇 TCP
(2)Ping Port : 80
(3)Advanced Details : 使用預設值
(4)設定完成後，點選 Next:Add EC2 Instances

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548589399807_Snipaste_2019-01-27_19-42-59.png)




## 8.Add EC2 Instances(Step5)

(1)選擇之前創建好的cc104_web_ec2_A
(2)設定好後，點選 Next Add Tags

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548590004996_Snipaste_2019-01-27_19-51-29.png)

## 9.Add Tags(Step6)

(1) Key:Name/Value:ELB-Project
(2)Key: cc104/Value:ELB-Project
(3)設定好後，點選 Review and Create

![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548751618566_789.png)

## 10.Review(Step7) 
- 確認ELB設定無誤後，點選右下角 Create
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548642189506_Snipaste_2019-01-28_10-22-19.png)

## 11.創建完成，點選 Close
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548642199525_Snipaste_2019-01-28_10-22-49.png)

## 12.可看到創建完成的ELB出現在頁面上
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F7555B1F121A49C0AEC35CF61707748B01D7620715C427202C63AF67A3C75991_1548750162220_1234.jpg)


