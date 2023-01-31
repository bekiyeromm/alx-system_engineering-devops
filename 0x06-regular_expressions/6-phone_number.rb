#!/usr/bin/env ruby
# ^ indicates start of expression
# \d refers digit only
# {10} match of 10 digits without any space
# $ end of expression marker
puts ARGV[0].scan(/^\d{10}$/).join
