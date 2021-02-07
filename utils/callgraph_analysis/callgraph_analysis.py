#
# python script with two parameters: fuzz-harness.cg fuzz.cg
# fuzz-harness.cg is generated by something like:
# clang++ -O3 -S -emit-llvm -I. -Iinclude fuzz-harness.cc | opt --analyze --basiccg -o fuzz-harness.cg
# fuzz.cg is generated with AFL_LLVM_LTO_CALLGRAPH=1
#
# 1. run c++filt on both .cg inputs
# 2. parse fuzz-harness.cg, remove all functions that just have on external call
#    keep an array of it's functions and the one it is calling
# 3. parse fuzz.cg, remove all functions that just have an external call.
# 4. loop on fuzz-harness.cg array, look for these functions in fuzz.cg,
#    remove them from both fuzz-harness.cg and fuzz.cg array when found and
#    add the callers into fuzz-harness.cg array instead.
# 5. resulting functions in fuzz-harness.cg array are unreachable
#
