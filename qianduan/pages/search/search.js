// pages/search/search.js
Page({

    /**
     * 页面的初始数据
     */
     /**
     * 页面的初始数据
     */
    data: {
        userInfo:"",
        isNull:0,
       movies:[],
       list:["吴京","徐克","黄渤"]

    },
    
  onLoad(e){
    var that=this;
    let user=wx.getStorageSync('user')
      console.log("获取到缓存",user)
      this.setData({userInfo:user})
    wx.request({
      url: 'http://127.0.0.1:8000/movie/alljson/',
      Headers : { ' content-type ' : ' application/JSON ' },
      success:function(e){ 
          var movies=e.data.data;
          console.log(movies);
          console.log('dsafasfads');
          that.setData({
              'movies':movies,
          })
      }
    })
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

  search(value){
var search=value.detail.value;
//console.log(search);
var old=this.data.list;
console.log(old)
    
if(old.length>=3){
    old.splice(2);
    old.unshift(search);
}
this.setData({
    'list':old,
})
console.log(old)
var that=this; 

    wx.request({
      url: 'http://127.0.0.1:8000/movie/search?value='+search,
      method:"GET",
      header:{
        'content-type':'application/text'
      },
      success:res=>{
          var movies=res.data.data;
         
      
        if(movies.length == 0){
            console.log("数据为空");
            that.setData({'isNull':1})
            console.log(that.data.isNull)
        }else{
            console.log(movies);
        that.setData({
            'movies':[],'isNull':0
        });
        that.setData({
            'movies':movies
            });
        console.log("movies",that.data.movies)
        } }
    })
  },

   // 搜索
  showInput() {
    this.setData({
      inputShowed: true,
    });
  },
  hideInput() {
    this.setData({
      inputVal: '',
      inputShowed: false,
    });
  },
  clearInput() {
    this.setData({
      inputVal: '',
    });
  },
  inputTyping(e) {
    this.setData({
      inputVal: e.detail.value,
    });
  },


  onShow() {
    console.log("onShow")
  let user=wx.getStorageSync('user')
  console.log("获取到缓存",user)
  this.setData({userInfo:user})
},
})