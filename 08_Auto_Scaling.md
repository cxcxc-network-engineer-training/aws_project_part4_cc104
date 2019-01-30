# 08_Auto Scaling

# 建立啟動組態(Create launch configuration)
## 1.在AWS Console 頁面選擇 EC2
![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548763293777_147.jpg)

## 2.先選擇左方窗格中的Launch Configuration，再點選Create launch configuration
![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548764540036_1000.jpg)

## 3.選擇AMI印象檔

(1)先點選左方Community AMIs
(2) 在上方欄位輸入: 1a15c
(3) 出現ami-1a15c77b
(4) 點選Select

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548642775301_Snipaste_2019-01-28_10-31-28.png)

## 4.Create Instance Type(選擇Instance類型)

(2)點選Next: Configuration details

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548642891089_Snipaste_2019-01-28_10-34-02.png)

## 5.Create Details(設定Instance的詳細資訊)

(1)Name : cc104_ASG
(2)IAM role: cc104_ec2_role
(3)Advanced Details:

    #!/bin/bash 
    yum update -y 
    yum install -y docker git awscli ruby 
    usermod -a -G docker ec2-user 
    service docker start 
    chkconfig docker on 

(4)選擇 Assign a public IP address to every instance(將公有IP 位址指派給每個執行個體)
(5)設定完成後，點選 Next Add Storage

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548643427671_Snipaste_2019-01-28_10-42-36.png)

## 6.Add Storage

(1)使用預設8G
(2)點選 Next Configure Security Group

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548643563724_Snipaste_2019-01-28_10-44-47.png)

## 7.Create Security Group

(1)選擇現有的防火牆
(2)選擇sg-0cc20e933fde8d51e(預設的VPC防火牆)
(3)再點選 Review

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548645967105_Snipaste_2019-01-28_11-09-30.png)

## 8.Review
- 確認設定無誤後，點選 Create launch configuration(建立起動組態)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548646155176_Snipaste_2019-01-28_11-28-36.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548646159056_Snipaste_2019-01-28_11-28-53.png)

## 9.Select an existing key pair

(1)選擇現有的 Key pair(cc104key)，再點選Create launch configuration

![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548751481163_456.jpg)



## 10.創建完成後的頁面
![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548752192811_111.jpg)

# 創建Auto Scaling group
## 1.先點選剛剛創建的
![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548751949073_41.jpg)

## 2.Create Auto Scaling Group
![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548763841934_6781548763810264.jpg)

## 3.Create Auto Scaling Group

(1)Group name : cc104-asg-elb-project
(2)Group size : start with “ 1“ instances
(3)Network : 選擇cc104_vpc
(4)Subnet : 選擇 cc104_web_Subnet
(5)Advanced Details

- Load Balancing : 勾選 Receive traffic from one or more load balancers
- Classic Load Balancers : 選擇創建好的ELB( cc104-elb)
- 設定好後點選 Next Configure scaling group
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548647852470_Snipaste_2019-01-28_11-46-25.png)

## 4.Configure scaling policies

(1)點選 Use scaling policies to adjust the capacity of this group

- Scale between ”1” and “4” instances

(2)Scale Group Size(預設)
(3)Metric type: 點選 Average CPU Utilization
(4)Target value: 60
(5)Instances need: 預設值
(6)設定完成後，點選 Next Configure Notifications

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548648476886_Snipaste_2019-01-28_12-07-39.png)

## 5.Configure Notifications

(1)建立通知

![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548766653439_7899.jpg)


(2)寄送通知到Topic(可選擇現有存在的，或是自己創建一個Topic)
(3)設定要被通知的信箱地址(此欄位輸入信箱地址)
(4)設定完成後，點選右下角Next Configure tags

![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548766889043_888888.jpg)

## 6.Configure Tags

(1)Key:Name/Value:asg-elb-project
(2)Key:cc104/Value:asg-elb-project
(3)設定完成後，點選Review

![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548654355076_Snipaste_2019-01-28_13-43-41.png)



## 7.Review
- 確認內容無誤後，點選 Create Auto scaling group
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548654433661_Snipaste_2019-01-28_13-46-57.png)

## 8.點擊 Close
![](https://d2mxuefqeaa7sj.cloudfront.net/s_44766B39D1BE4B8BB1DC5E3A308DF38A07E9CA4C84846794E82C5BEE00E3DAC3_1548654620075_Snipaste_2019-01-28_13-49-22.png)

## 9.創建完成的Auto Scaling group有出現在畫面上
![](https://d2mxuefqeaa7sj.cloudfront.net/s_FD4485C79C7006A363D9AD4FE6D8A87E476228F0AB852BEE5168EC44C52EE493_1548767421414_555.jpg)


