cd ../spacal-simulation
time ./build/FibresCalo spacal-base_OnlyGAGG.cfg /calo/outputs/out |& tee /calo/outputs/logs.txt
cd /calo
python ../spacal-simulation/rootToNumpy.py ./outputs/out.root
python convert_file.py
cp ../spacal-simulation/spacal-base_OnlyGAGG.cfg ./outputs/
cp ../spacal-simulation/gps_electron.mac ./outputs/
# cp -r ./outputs /outputs
