Y_COUNT=$(grep -c "=y$" $1)
N_COUNT=$(grep -c "is not set$" $1)
M_COUNT=$(grep -c "=m$" $1)
SHA=$(sha256sum $1 | cut -c-12)

echo "y${Y_COUNT}-m${M_COUNT}-n${N_COUNT}-s${SHA}"
