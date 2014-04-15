<?php
$filename = 'E:\\xampp\\htdocs\\syc\\test.txt';
$somecontent = date("Y-m-d H:i:s")."\n";

// 首先我们要确定文件存在并且可写。
if (is_writable($filename)) {

    // 在这个例子里，我们将使用添加模式打开$filename，
    // 因此，文件指针将会在文件的末尾，
    // 那就是当我们使用fwrite()的时候，$somecontent将要写入的地方。
    if (!$handle = fopen($filename, 'a')) {
         echo "can not open $filename";
         exit;
    }

    // 将$somecontent写入到我们打开的文件中。
    if (fwrite($handle, $somecontent) === FALSE) {
        echo "can not write $filename";
        exit;
    }

    echo 0;

    fclose($handle);

} else {
       echo "file $filename can not write";
}