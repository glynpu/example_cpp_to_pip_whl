source ~/env/bin/py3/bin/activate
 g++ -O3 -Wall -shared -std=c++11 -fPIC `python -m pybind11 --includes` cpp/arithmetic.cpp -o pipeg/arithmetic.cpython-36m-x86_64-linux-gnu.so `python3-config --ldflags` -I/usr/include/python3.6m/
python setup.py bdist_wheel
pip install dist/pipeg-0.0.1-py3-none-any.whl
python -c "import pipeg; print(pipeg.arithmetic.add(1,2))"
