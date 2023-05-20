# kaitai_examples
Kaitai Examples

## Install prerequisites
```
apt-get update
apt-get install -y --no-install-recommends ruby openjdk-8-jre-headless python3-pip
wget https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.10/kaitai-struct-compiler_0.10_all.deb
dpkg -i kaitai-struct-compiler_0.10_all.deb
rm kaitai-struct-compiler_0.10_all.deb
gem install kaitai-struct-visualizer
pip install kaitaistruct
```

## Compile gif.ksy and run
```
./generate_python_code.sh
./main.py
```

## Visualize tree.gif
```
ksv tree.gif gif.ksy
```
