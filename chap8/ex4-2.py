s1 = 'this is undoubtedly right';
s2 = 'this is indubitably wrong';

out = list(set(s1) & set(s2));
out.remove(' ');

print("common chars are:", end=' ');
print(*out, sep=', ');
