# initial-scribble-collector

We have 1,000 video sequences to be labeled. We divide these sequences into 10 lists, i.e., each list contains 100 video sequences. 

## Task 
List ID | Jia 1 | Xianing 2 | Jiale 3 | Lei 6 | Shenhan 7
:---:|:---:|:---:|:---:|:---:|:---:|
1       |O|O|#||
2       |||O|O|O
3       |||O||#
4       |||O||O
5       |||O||O
6       |||O||O
7       |||||
8       |||||
9       |||||
10     |||||
11     |||||

## Download Dataset 
You can download Youtube-VOS dataset [here](http://10.19.124.26:8000/d/f274b8e2c98649b2b575/).

## Upload Your Scribbles
When you finished your current task, please zip the `Scribbles` directory and name it as `user_id-list_id.zip`, such as `001-1.zip`. And upload the zip file to [here](http://10.19.124.26:8000/u/d/cc87c1773bab4029ac5a/), and we will assign another list to you.  

## A Guide to Scribble-Collector

### Environment configuration
```bash
pip3 install -r requirements.txt
```

### Start the GUI
```bash
python3 scribble_collector.py --dataset_dir /path/to/dataset --user_id your_id  --list_id your_task_list_id 
```

### Hotkeys
Key | Function
:---:   | :---:
D       | Next frame
A       | Last frame
R       | Clear current scribbles  
Space       | Save current scribbles 

## Attention
* If a certain sequence can't be labeled properly you can click on `Wrong Sequence` button to mark it. The program will keep recording **labeled sequences** and **error sequences**, and save them to different JSON files, such as `001_log.json`. You can find it in the `Scribbles` directory. 
 
* Every time you click `Save` or `Wrong Sequence`, the program will automatically switch to the next sequence.

* If you accidentally quit the program, don't pannic. All the JSON files that you've generate will be kept. When you re-open it, the program will start from where you left.
  
* Please avoid drawing on the boundary of the mask, since such kind of scribbles will influence our segmentation algorithm. 

* Make sure that the frame you select can best represent all objects of interest. 
  
## Wrong Sequence Cases

### Case 1: The man is mislabeled as the bus. 
![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/0.png)

### Case 2: No mask annotations in some frames. 
![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/3.png)

![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/2.png)

### Case 3: No frame consists of all objects. 
![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/4.png)

![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/6.png)

### Case 4: The scale of the object is too small. 
![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/5.png)

### Case 5: Image Visualization Error
![](http://10.19.124.26:8000/thumbnail/4b7e5a90-b7c9-433b-9ee5-5b5298ede12b/1024/wrong_cases/1.png)



