app.service('goodsService',function ($http) {
    //增加
    this.add=function (entity) {
        var url="/goods/add.shtml";
        return $http.post(url,entity);
    }
    //修改
    this.update=function (entity,password) {
        var url="/goods/update?password="+password;
        return $http.post(url,entity);
    }
    //删除
    this.delete=function (ids) {
        var url="/goods/delete.shtml"
        return $http.post(url,ids);
    }
    //根据id查询
    this.findOne=function (sku) {
        var url="/goods/selectOne?id="+sku;
        return $http.get(url);
    }
    //分页查询所有

    this.findAll=function (page,size,searchEntity) {
        var url='/goods/selectAll';
        // var url = '/goods/selectAllByLimit?page='+page+'&size='+size;
        // return $http.get(url,searchEntity);
        return $http.get(url);
    }

});