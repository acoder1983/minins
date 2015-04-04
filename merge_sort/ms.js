function mergesort(unsorted){
	if(unsorted.length < 2){
		return unsorted;
	}
	else{
		var arr1=mergesort(unsorted.slice(0, unsorted.length/2-1));
		var arr2=mergesort(unsorted.slice(unsorted.length/2));
		var sorted = new Array();
		var i = 0;
		var j = 0;
		while(i < arr1.length || j < arr2.length)
		{
			if (i == arr1.length || (j != arr2.length && arr1[i] > arr2[j])) {
				sorted.push(arr2[j]);
				++j;
			} else {
				sorted.push(arr1[i]);
				++i;
			}
		};
		return sorted;
	}
};

var actual = mergesort([2,1]);
var ret = true;
var expect = [1,2];
for (var i = 0; i < expect.length; ++i) {
	if(actual[i] != expect[i]){
		ret = false;
		break;
	}
};
document.body.innerHTML = ret ? "success":"failed";