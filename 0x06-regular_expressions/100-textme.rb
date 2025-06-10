#!/usr/bin/env ruby
#!/usr/bin/env ruby
line = ARGV[0]
if line
  # look for [from:...] [to:...] [flags:...]
  m = line.match(/\[from:([^\]]+)\].*?\[to:([^\]]+)\].*?\[flags:([^\]]+)\]/)
  puts "#{m[1]},#{m[2]},#{m[3]}" if m
end
