// pages/login_sq/login_sq.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      userInfo:""
    },
  
    login(){
      var that=this
      console.log("denglu")
      wx.getUserProfile({ 
        desc: '用于完善会员资料',//展示在弹框中
        success(res){ 
          console.log("授权成功",res.userInfo)
          that.setData({userInfo:res.userInfo})
          wx.setStorageSync('user', res.userInfo)//把用户信息存到本地
        },
        fail(res){
          console.log("授权失败",res)
        }
      })
    },
  
    //退出登录
    logout(){
      this.setData({userInfo:''})
      wx.setStorageSync('user', null)
  
    },
  
  
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {
      console.log("onLoad")
      let user=wx.getStorageSync('user')
      console.log("获取到缓存",user)
      this.setData({userInfo:user})
    },
  
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady() {
  
    },
  
    /**
     * 生命周期函数--监听页面显示
     */
    onShow() {
        console.log("onShow")
      let user=wx.getStorageSync('user')
      console.log("获取到缓存",user)
      this.setData({userInfo:user})
    },
  
    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide() {
  
    },
  
    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {
  
    },
  
    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {
  
    },
  
    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {
  
    },
  
    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {
  
    }
  })