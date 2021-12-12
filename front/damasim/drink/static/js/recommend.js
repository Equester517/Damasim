var imageList=[] //이미지리스트
for(i=1;i<70;i++) {
	if(i<10)
		imageList.push('bev_00'+i+'.jpg')
	else if(i>=10)
		imageList.push('bev_0'+i+'.jpg')
}