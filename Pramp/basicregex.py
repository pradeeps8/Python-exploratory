def is_match(text, pattern):
  return match_pattern(text, pattern, 0,0)
 
STAR = '*'
DOT = '.'

def match_pattern(text, pattern, txt_indx, pat_indx):
  ##print(text, pattern, txt_indx, pat_indx)
  if(pat_indx >= len(pattern)):
    return True
  
  if(pat_indx + 1 < len(pattern)):
    if(pattern[pat_indx+1] == STAR):
      while(text[txt_indx] == pattern[pat_indx]):
          txt_indx += 1
      return match_pattern(text, pattern, txt_indx, pat_indx+2)
    else:
      if (text[txt_indx] != pattern[pat_indx]) and (pattern[pat_indx] != DOT):
        return False
      elif ((pat_indx + 1) >= len(pattern)) and ((txt_indx + 1) < len(text)) :
        return False    
      else :
        return match_pattern(text, pattern, txt_indx+1, pat_indx+1)
  
  else:
    if (text[txt_indx] != pattern[pat_indx]) and (pattern[pat_indx] != DOT):
        return False
    elif ((pat_indx + 1) >= len(pattern)) and ((txt_indx + 1) < len(text)) :
        return False    
    else :
        return match_pattern(text, pattern, txt_indx+1, pat_indx+1)  
      
print (is_match("abc", "a*bc"))
print (is_match("ac", "a*.c"))