# initial-scribble-collector

Since there are totally 1000 sequences to be labled, we've divided them into 10 lists, which means each list contains 100 sequences. Please check the **Task** table below, and start your work once with a list.

So, every time you start the GUI, three arguments are needed:
```
--dataset_dir
--user_id
--list_id
```

When you have finished a certain list, please zip the `Scribble` directory and name it as `user_id-list_id.zip`, such as `001-1.zip`.

Please send the zip file to Shenhan Qian, and the next list assignment will come soon.




## Task
List_id\User_id|Zhenjie Chai 1|Xianing Chen 2 |Jiale Xu 3|Jia Zheng 4|Zhaoyuan Yin 5|Lei Jin 6|Shenhan Qian 7
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
1       |O|O|#||||
2       ||||O|O|O|
3       ||O|O||||#
4       ||O|O||||O
5       ||O|O||||O
6       ||O|O||||O
7       |||||||O
8       ||||O|O|O|
9       ||||O|O|O|
10      ||||O|O|O|


## Environment configuration
```bash
pip3 install -r requirements.txt
```

## Start the GUI
```bash
python3 scribble_collector.py --dataset_dir /path/to/dataset --user_id your_id  --list_id your_task_list_id 
```

## Hotkeys
Key | Function
:---:   | :---:
D       | Next frame
A       | Last frame
R       | Clear current scribbles  
Space       | Save current scribbles 

## Download Dataset 
This is the complete Youtube-VOS dataset, please download 
via [here](http://10.19.124.26:8000/d/f274b8e2c98649b2b575/).

## Attention
* If a certain sequence can't be labeled properly you can click on `Wrong Sequence` 
button to mark it. The program will keep recording **labeled sequences** and 
**error sequence**, and save them to a Json file, such as `001_log.json`. You can 
find it in the `Scribbles` directory.
 
* Every time you click `Save` or `Wrong Sequence`, the program will automatically
switch to the next sequence.

* If you accidentally quit the program, don't Pannic. All the JSON files that
 you've generate will be kept. When you re-open it, the program will start 
 from where you left.
  
* Please avoid drawing on the boundary of the mask, since such kind of scribbles 
will influence our segmentation algorithm. 

* Make sure that the frame you select can best represent all objects of interest. 
  


