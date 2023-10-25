function show(){
    let elements = document.getElementsByClassName('button_picture_hide_first');
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = "block"; // 修改为所需的显示方式
    }
}



url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
fetch(url)
.then(response => response.json())
.then(data => {
    let info = data['result']['results'];
    let name = [];
    let pictures = [];
    for (i of info){
        name.push(i['stitle']);
        let picture = i['file'];
        let index = picture.toLowerCase().indexOf('jpg');
        pictures.push(picture.slice(0,index+3));
    }
    for (let i=1;i<28;i++){

        // 文字處理
        let textNode = document.createTextNode(name[i]);

        let change_text_id = 'top'
        change_text_id += i.toString()

        let divElement = document.getElementById(change_text_id);

        while (divElement.firstChild) {
            divElement.removeChild(divElement.firstChild);
        }

        divElement.appendChild(textNode);



        // 圖片處理
        let change_pic_id = 'top_pic'
        change_pic_id += i.toString()

        // 获取要更改图片 URL 的 <img> 元素
        let imgElement = document.getElementById(change_pic_id);

        // 设置新的图片 URL
        let newImageUrl = pictures[i];
        console.log(name[i],pictures[i]);
        // 更新 <img> 元素的 src 属性
        imgElement.src = newImageUrl;


    }

    // 圖片處理
    
})
.catch(error => {
    // 处理错误
    console.error('请求出错:', error);
});
