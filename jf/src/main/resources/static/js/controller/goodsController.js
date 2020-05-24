//创建一个controller
app.controller('goodsController',function ($scope,$http,goodsService) {


    //定义一个searchEntity对象，防止空指针
    $scope.searchEntity={};

    //查询所有品牌列表
    $scope.getPage=function (page,size) {
        //请求地址
        console.log("getPage",page,size);

        $scope.list=[]
        $scope.href=[]
        goodsService.findAll(page,size,$scope.searchEntity).success(function (response) {
            // console.log(response)
            // //获取响应数据  先接受集合数据
            // $scope.list=response;

            $scope.list=[]
            for(var i=0;i<response.length;i++){
                // console.log("-----");
                // console.log(response[i]);
                var reg = /(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?/g;
                // v = response[i].replace(reg, "<a href='$1$2'>$1$2</a>").replace(/\n/g, "<br />");
                // v = reg.exec(response[i]);
                v = response[i].match(reg);
                // console.log(v);

                // $scope.href.push(v);
                var tmp  ={"content":response[i],"href":v};
                $scope.list.push(tmp);
            }

            console.log("$scope.list",$scope.list)
            // //给分页参数赋值
            $scope.paginationConf.totalItems=response.total;
        });
    }


    //创建save方法
    $scope.save=function () {
        var result=null;
        //如果id!=null，则执行修改
        console.log($scope.entity)
        // if($scope.entity.sku!=null){
        //     result=goodsService.update($scope.entity,$scope.password);
        // }else{
        //     result=goodsService.add($scope.entity)
        // }
        result=goodsService.add($scope.entity.content)

        result.success(function (response) {
            if(response.success){
                //增加成功，刷新页面
                $scope.getPage(1,10);
            }else{
                alert(response.msg);
            }
        })
    }


    //根据DI查询   id:品牌ID
    $scope.findOne=function (sku) {
        goodsService.findOne(sku).success(function (response) {
            // console.log(response)
            $scope.entity=response.obj;
        });
    }


    //删除方法
    $scope.delete=function () {
        //执行删除
        goodsService.delete($scope.selectIds).success(function (response) {
            if(response.success){
                //删除成功，重新加载页面
                $scope.getPage(1,10);
            }else{
                alert(response.message);
            }
        })
    }


    //定义一个集合存储当前选中的id
    $scope.selectIds=[];


    //给复选框一个点击事件，如果是勾选，则将勾选的ID加入到$scope.selectIds=[]。
    //				    如果是取消勾选，则将该ID从$scope.selectIds=[]移除。
    $scope.updateSelection=function ($event,id) {
        //如果是勾选，则将勾选的ID加入到$scope.selectIds=[]。
        if($event.target.checked){
            //往集合中添加数据使用push
            $scope.selectIds.push(id);
        }else{
            //获取ID在集合中的下标
            var index = $scope.selectIds.indexOf(id);

            //移除对应下标的数据,splice表示将集合中的对应下标数据移除一次
            $scope.selectIds.splice(index,1);
        }

        console.log($scope.selectIds);
    }


    /***
     * 分页控件配置
     * currentPage:当前页
     * totalItems:共有多少条记录
     * itemsPerPage:每页显示多少条
     * perPageOptions:每页多少条选项条
     * onChange:参数发生变化时执行
     * */
    $scope.paginationConf = {
        currentPage: 1,
        totalItems: 10,
        itemsPerPage: 10,
        perPageOptions: [10, 20, 30, 40, 50],
        onChange: function(){
            //监控paginationConf参数的变化:当分页参数发生变化，我们可以执行分页查询
            $scope.getPage($scope.paginationConf.currentPage,$scope.paginationConf.itemsPerPage);
        }
    };

    $scope.qrDict={}
    $scope.qrFlags=[]
    $scope.qr = function (h) {
        var index=$scope.qrFlags.indexOf(h)
        if (index==-1){
            // new QRCode(document.getElementById(h), h);
            var qrcode = new QRCode(document.getElementById(h),
                {
                text: h,
                width: 210,
                height: 210,
                colorDark : "#000000",
                colorLight : "#ffffff",
                correctLevel : QRCode.CorrectLevel.H
            });
            $scope.qrFlags.push(h);

        }

        //console.log($scope.qrDict)
        //console.log($scope.qrDict.hasOwnProperty(h),$scope.qrDict.hasOwnProperty('aaa'))

        // if($scope.qrDict.hasOwnProperty(h)){
        //     $scope.qrDict[h].clear();
        //     delete $scope.qrDict[h];
        // }else{
        //     var qrcode = new QRCode(document.getElementById(h),
        //         {
        //             text: h,
        //             width: 200,
        //             height: 200,
        //             colorDark : "#000000",
        //             colorLight : "#ffffff",
        //             correctLevel : QRCode.CorrectLevel.H
        //         });
        //     $scope.qrDict[h]=qrcode;
        // }
    }

    $scope.qr2 = function (h) {

        // alert(h)
        var qrcode = new QRCode(document.getElementById(h),
            {
                text: h,
                width: 210,
                height: 210,
                colorDark: "#000000",
                colorLight: "#ffffff",
                correctLevel: QRCode.CorrectLevel.H
            });


    }


});