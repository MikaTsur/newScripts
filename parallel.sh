for b in {0..1} ; do
    t=$(($a + $b))
    echo "now running test.py with t=${t}" >> log.txt
    python minmax_new.py $m $t &
done
echo "now waiting..." >> log.txt
