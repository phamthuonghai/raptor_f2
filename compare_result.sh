echo "============================================"
echo "||           Result compare               ||"
echo "============================================"
echo "================ 10 ==================="
python ./src/result_cmp.py -i ./lab/PyRaptor/10/Result/original/Raptor_sg.csv -o ./lab/Haskell/10/Result/original/Raptor_sg.csv

echo "================ 50 ==================="
python ./src/result_cmp.py -i ./lab/PyRaptor/50/Result/original/Raptor_sg.csv -o ./lab/Haskell/50/Result/original/Raptor_sg.csv

echo "================ 100 =================="
python ./src/result_cmp.py -i ./lab/PyRaptor/100/Result/original/Raptor_sg.csv -o ./lab/Haskell/100/Result/original/Raptor_sg.csv

echo "================ 500 =================="
python ./src/result_cmp.py -i ./lab/PyRaptor/500/Result/original/Raptor_sg.csv -o ./lab/Haskell/500/Result/original/Raptor_sg.csv

echo "================ 1000 ================="
python ./src/result_cmp.py -i ./lab/PyRaptor/1000/Result/original/Raptor_sg.csv -o ./lab/Haskell/1000/Result/original/Raptor_sg.csv

echo "================ 5000 ================="
python ./src/result_cmp.py -i ./lab/PyRaptor/5000/Result/original/Raptor_sg.csv -o ./lab/Haskell/5000/Result/original/Raptor_sg.csv

echo "================ 10000 ================"
python ./src/result_cmp.py -i ./lab/PyRaptor/10000/Result/original/Raptor_sg.csv -o ./lab/Haskell/10000/Result/original/Raptor_sg.csv