GNU Radio LTE Receiver
================

The *gr-lte* project is an Open Source Software Package which aims to provide a GNU Radio LTE Receiver to receive, synchronize and decode LTE signals. Its development was focused on modularity. This makes the project easy to extend and reuse its blocks.

This project was initiated as a Bachelor thesis at the *Communication Engineering Lab (CEL)* at the *Karlsruhe Institute of Technology (KIT)*, Germany, <http://www.cel.kit.edu>.


The Idea
-------------
This project aims to provide a modular environment for an LTE downlink receiver. All blocks should be replacable. e.g. introduce a new channel estimator block with more advanced algorithms. On the other hand it should be fairly easy to add new blocks to decode additional physical channels.<br>
The block design aims to be modular and reusable. Where possible GR blocks are used.<br>
Furthermore message ports are used for configuration on runtime. This is supposed to make the control flow visible to users and thus better understandable.


Requirements
------------
- GNU Radio 3.7
    - all code was moved to GR 3.7 API.
    - old code is not removed so far but should be regarded deprecated.
    
- GR 3.6.5.1 (deprecated)
    - message passing API is necessary
    - all the latest bug fixes
    - project used to use GR 3.6 API
    
- MATLAB (deprecated)
    - R2011b tested
    - m-files are replaced by Python/Numpy/Scipy code which offers greater flexibility and connectivity to GNU Radio.
    - for .m-files
    - If you want, have a look at the m-files



Build/Install instructions for Linux
------------------------------------

1. Get, build and install GNU Radio from <http://www.gnuradio.org>

2. Get *gr-lte* from github

3. Configure it using CMake<br>
Assuming you are already in the project folder<br>
`cd code/`<br>
`mkdir build`<br>
`cp cmake_install.sh build/`<br>
`cd build`<br>
`./cmake_install.sh`<br>  
This will just run a little script to aid with project setup for Code::Blocks<br>
Otherwise run `cmake ..`

4. run *sudo make install*<br>
`make -jX` where X is a number of choice (Often the number of cores available)<br>
`sudo make install` (make it available in GRC)

5. compile hierarchical GRC blocks<br>
hierarchical GRC blocks must be generated by opening them in GRC and clicking `Generate`. Afterwards reload blocks or restart GRC. This makes the hier blocks available in GRC just as all the other blocks.

5. Have fun<br>
If everything runs without errors the -gr-lte blocks should be available in GRC
