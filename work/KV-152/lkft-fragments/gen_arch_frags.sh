cat */arm.frag | sort | uniq > arm.frag
cat */x86_64.frag | sort | uniq > x86_64.frag
cat */i386.frag | sort | uniq > i386.frag
cat */arm64.frag | sort | uniq > arm64.frag
cat *.frag | sort | uniq > lkft.frag
