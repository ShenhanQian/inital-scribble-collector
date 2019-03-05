# initial-scribble-collector

### Environment configuration
```bash
pip3 install -r requirements.txt
```

### Start the GUI
```bash
python3 scribble_collector.py --dataset_dir /path/to/dataset --user_id your_id
```

### Hotkeys
Key | Function
:---:   | :---:
D       | Next frame
A       | Last frame
R       | Clear current scribbles  
Space       | Save current scribbles 

### Download Dataset 
This is the complete Youtube-VOS dataset, please download 
via [here](http://10.19.124.26:8000/d/f274b8e2c98649b2b575/).

### User ID

User ID | Name
:---:   | :---:
1       | Zhenjie Chai
2       | Xianing Chen
3       | Jiale Xu 

### Attention
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
  


