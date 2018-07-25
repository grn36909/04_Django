# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB07 QuerySet API
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-models.html)  

从数据库中查询出来的结果一般是一个集合，这个集合叫做 `QuerySet`  

### 1.1 创建对象的方法：
```python
# 方式1
Person.objects.create(name=name,age=age)  
```

```python
# 方式2
p = Person(name="WZ", age=23)`  
p.save()  
```
```python
# 方式3
p = Person(name="TWZ")  
p.age = 23
p.save()
```

```python
# 方式4
Person.objects.get_or_create(name="WZT", age=23)
# 这种方法是防止重复很好的方法，但是速度要相对慢些。  
# 返回一个元组，第一个为`Person`对象，第二个为`True`或`False`, 新建时返回的是`True`, 已经存在时返回`False`.  
```

### 1.2 获取对象的方法

```python
# 方式1
Person.objects.all()  
```

```python
# 方式2
Person.objects.all()[:10]  
# 切片操作，获取10个人，不支持负索引，切片可以节约内存
```

```python
# 方式3
Person.objects.get(name=name)  
# get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter  
```

```python
# 方式4
Person.objects.filter(name="abc")  
# 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人  
```

```python
# 方式5
Person.objects.filter(name__iexact="abc")  
# 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件  
```

```python
# 方式6
Person.objects.filter(name__contains="abc")  
# 名称中包含 "abc" 的人  
```

```python
# 方式7
Person.objects.filter(name__icontains="abc")  
#名称中包含 "abc"，且abc不区分大小写  
```

```python
# 方式7
Person.objects.filter(name__regex="^abc")  
# 正则表达式查询  
```

```python
# 方式8
Person.objects.filter(name__iregex="^abc")  
# 正则表达式, 不区分大小写  
```

filter是找出满足条件的，当然也有排除符合某条件的  

```python
# 方式10
Person.objects.exclude(name__contains="WZ")  
# 排除包含 WZ 的Person对象  
```

```python
# 方式11
Person.objects.filter(name__contains="abc").exclude(age=23)  
# 找出名称含有 abc, 但是排除年龄是23岁的  
```

### 1.3 删除对象的方法

```python
# 方式1
Person.objects.filter(name__contains="abc").delete() 
# 删除 名称中包含 "abc"的人  
```

```python
# 方式2
people = Person.objects.filter(name__contains="abc")  
people.delete()  
```

方式2的效果也是一样的，Django 实际只执行一条 SQL 语句。  

### 1.4 更新对象的方法

1. 批量更新，适用于 `.all()`  `.filter()`  `.exclude()` 等后面 ~~(危险操作，正式场合操作务必谨慎)~~  

```python
# 方式1
Person.objects.filter(name__contains="abc").update(name='xxx') 
# 名称中包含 "abc"的人 都改成 xxx  
```

```python
# 方式2
Person.objects.all().delete() 
# 删除所有 Person 记录  
```

2. 单个 object 更新，适合于 `.get()`, `get_or_create()`, `update_or_create()` 等得到的 obj，和新建很类似。

```python
> twz = Author.objects.get(name="WeizhongTu")  
> twz.name = "WeizhongTu"  
> twz.email = "tuweizhong@163.com"  
> twz.save()  
# 最后不要忘了保存！！！  
```

### 1.5 可迭代

`QuerySet` 是可迭代的，比如：  

```pythion
es = Entry.objects.all()
for e in es:
    print(e.headline)
```
`Entry.objects.all()` 或者 `es` 就是 `QuerySet` 所查询到的所有的 `Entry` 条目。  

**注意事项：**

1. 如果只是检查 `Entry` 中是否有对象，应该用 `Entry.objects.all().exists()`  

2. `QuerySet` 支持切片 `Entry.objects.all()[:10]` 取出10条，可以节省内存  

3. 用 `len(es)` 可以得到`Entry`的数量，但是推荐用 `Entry.objects.count()` 来查询数量，后者用的是`SQL：SELECT COUNT(*)`  

4. `list(es) `可以强行将 `QuerySet` 变成 列表

### 1.6 可使用 pickle 读写到磁盘

```python
import pickle
query = pickle.loads(s)     # Assuming 's' is the pickled string.
qs = MyModel.objects.all()
qs.query = query            # Restore the original 'query'.
```

### 1.7 查询结果排序

```python
Author.objects.all().order_by('name')   # 按作者名称排序
Author.objects.all().order_by('-name')  # 在 column name 前加一个负号，可以实现倒序
```

### 1.8 支持链式查询

```python
Author.objects.filter(name__contains="WeizhongTu").filter(email="tuweizhong@163.com")
Author.objects.filter(name__contains="Wei").exclude(email="tuweizhong@163.com")
 
Person.objects.filter(name__contains="abc").exclude(age=23)
# 找出名称含有abc, 但是排除年龄是23岁的  
```

### 1.9 不支持负索引

```python
Person.objects.all()[:10]     # 切片操作，前10条
Person.objects.all()[-10:]    # 会报错！！！
 
# 1. 使用 reverse() 解决
Person.objects.all().reverse()[:2] # 最后两条
Person.objects.all().reverse()[0] # 最后一条
 
# 2. 使用 order_by，在栏目名（column name）前加一个负号
Author.objects.order_by('-id')[:20] # id最大的20条
```
