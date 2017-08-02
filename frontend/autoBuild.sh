echo "构建开始"
npm run build
echo "构建结束"

echo "git add ."
git add .
echo "git commit -m 'auto commit'"
git commit -m 'auto commit'
echo "git push origin master"
git push origin master

echo "上传完毕"
