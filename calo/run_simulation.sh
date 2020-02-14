python set_parameters.py $1 $2 |& tee /calo/outputs/logs.txt
cd ../spacal-simulation
time ./build/FibresCalo spacal-base_OnlyGAGG.cfg /calo/outputs/out |& tee -a /calo/outputs/logs.txt
cd /calo
python ../spacal-simulation/rootToNumpy.py ./outputs/out.root |& tee -a /calo/outputs/logs.txt
python convert_file.py |& tee -a /calo/outputs/logs.txt
cp ../spacal-simulation/spacal-base_OnlyGAGG.cfg ./outputs/
cp ../spacal-simulation/gps_electron.mac ./outputs/
# cp -r ./outputs /outputs
