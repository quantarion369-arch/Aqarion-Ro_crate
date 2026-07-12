cd lean
lake exe cache get
lake build
lake exe aqarion_verify
python ../verification/lean_ci.py --log ../reports/lean_output.log
