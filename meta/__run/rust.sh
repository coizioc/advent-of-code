cd rust
cargo run $1 $2 || {
    cd ..
    exit 1
}
cd ..

exit 0