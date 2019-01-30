# 13_Route 53

# (一) Route53公有託管區說明
## (1)先至AWS主控台選擇 Route 53
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548820924345_r2.jpg)



## (2) 進入Route53的Console後，先點選Hosted zones ， 再點選Create Hosted Zone(建立公有託管區域) ，出現右側窗格
- Domain Name：ucloudchain.me. (此欄位輸入要將流量路由所至的網域)
- Type：選擇Public Hosted Zone (接受公有託管區域的預設值)
- 設定完成後，點選 Create 
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548819119783_r1.jpg)

## (3)點選左邊的Hosted zones後，再選取已註冊申請的公有託管區域(例如ucloudchain.me.)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_A863EB30DF45B0EA891DD9F59F923FC93AA2F6BABA47D650D002EF0354EBD3FB_1548727997960_002.jpg)

##   (4) 在左側窗格選擇 Instances後 ，選取一台EC2主機
- 此時可在右下方看到 IPv4 Public IP: 13.231.151.148 
![](https://d2mxuefqeaa7sj.cloudfront.net/s_A863EB30DF45B0EA891DD9F59F923FC93AA2F6BABA47D650D002EF0354EBD3FB_1548728002445_003.jpg)



## (5) 再回到Route 53設定，點選左側的Hosted zones，再點選上方的 Create Record Set，此時出現右側視窗:
- NAME:(輸入想取的名稱)
- TYPE:(有各類型資料，選擇A-IPV4 address)
- 設定完成後，點選下方Create，確認對應區已新增一筆資料
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548821352381_33.jpg)



## (6)選取剛才創建的物件後，點選上方Test Record Set
![](https://d2mxuefqeaa7sj.cloudfront.net/s_A863EB30DF45B0EA891DD9F59F923FC93AA2F6BABA47D650D002EF0354EBD3FB_1548728018936_005.jpg)

## (7)接下來看到Check response from Route 53測試視窗
- Hosted zone : **ucloudchain.me.**
- Record name :  **cc104-jimmy888** 
- Type* : **A** (DNS紀錄類型是A，代表地址紀錄)
- 設定完成後，點選下方 **Get respone** 
- 最後，會在右邊視窗看到 **Record name** 解析出 IP為  **13.231.151.148** 
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548821874070_555.jpg)

## (8) 打開命令提示字元，分別輸入
    nslookup
    cc104-jimmy888.ucloudchain.me.

最後以 **cc104-jimmy888.ucloudchain.me. 解析出IP Adress : 13.231.152.160**



![](https://d2mxuefqeaa7sj.cloudfront.net/s_A863EB30DF45B0EA891DD9F59F923FC93AA2F6BABA47D650D002EF0354EBD3FB_1548813111379_007.jpg)



# (二)Route53私有託管區說明：
## (1)先點選Hosted zones，再點選上方的Create Hosted Zone(建立私有託管區域)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548826607972_550.jpg)

## (2)在右方出現Create Hosted Zone的視窗  
- Domain Name ：**vcloudlab.pro.**
- Type ： 選取 Private **Hosted Zpne for Amazon VPC**
- VPC ID ：**vpc-091c46c6976d353e4 | ap-northeast-1**
- 設定完成後，點選下方 **Create****，託管區域即創建完成**
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548826769689_44.jpg)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548832775297_pri.jpg)

## (3)在私有託管區域建立角色
- 點選 Create Record Set後，出現右側窗格
  - Name : (輸入想取的名稱)
  - Type :  A-IPV4 address 
  - Value :  12.231.152.160 
  - 設定完成後，點選 Create 


![](https://d2mxuefqeaa7sj.cloudfront.net/s_A863EB30DF45B0EA891DD9F59F923FC93AA2F6BABA47D650D002EF0354EBD3FB_1548831735325_012.jpg)

- 創建好的Record Set已出現在畫面中
![](https://d2mxuefqeaa7sj.cloudfront.net/s_6F608A652C4EF2162F6F1A7F9066806FB53A0023BF3B7F9FF12DFA0D2B224210_1548832439867_r53.jpg)


