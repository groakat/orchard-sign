mkdir -p "../output/laser_ready/"

for FILE in ../output/orchard*.svg
do
    inkscape $FILE --export-text-to-path -o "../output/laser_ready/ready_$(basename ${FILE})";
done