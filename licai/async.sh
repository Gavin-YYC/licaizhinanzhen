echo "开始同步..."
cp ../python_finance/static/index.html ./static/index.html
cp ../python_finance/static/build/app.js ./static/build/app.js
echo "同步完成！"


echo "同步服务器数据"
echo "git push origin :1"
git pull origin :1
echo "git add ."
git add .
echo "git commit -m 'f'"
git commit -m "f"
echo "git push origin master:1"
git push origin master:1
echo "上传完成"
