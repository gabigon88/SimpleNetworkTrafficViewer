# SimpleNetworkTrafficViewer
本次練習嘗試使用Electron，也是我第一次撰寫桌面應用程式  
關於Electron: 一個使用 JavaScript、HTML 和 CSS 建構跨平台桌面應用程式  
[官方網站](https://electronjs.org/)  

應用程式的內容則是  
用python練習寫偵測網路流量的程式  
想到過去從來沒有寫過流量相關的練習  
心血來潮找了一下python套件就寫了  
網路流量的獲取 使用psutil套件，是一個系統監控模組  

GUI套用bootstrap的樣板  
獲取流量方面原本想用JS處理  
但查了一下 用JS似乎實現似乎不太容易  
就決定藉由JS的spawn以shell命令執行python  

## 執行方式
```bash
# Install python dependencies
pip install psutil
# Install dependencies
npm install
# Run the app
npm start
```  

## 執行畫面
<img src="./picture01.gif"/>  
