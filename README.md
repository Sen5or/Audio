# Audio

## Modified Files:

libfreenect.modify/examples/wavrecord.c
							CMakeList.txt

## How to record voice

cd libfreenect
mkdir build
cd build
cmake -L .. # -L lists all the project options
cd examples
make
cd ../bin

Then execuable file is in the folder, it will record 4 channel voice use Kinect, and then sample a 16 bit * 16000 sample.wav from channel0.wav

## How to identify

