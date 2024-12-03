import sys
import argparse
from pathlib import Path
from collections import Counter

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from utils.display_results import display_result

class DayOneSolution2024:
  input = 'input.txt'
  test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.test_input,'r').read() if test else open(self.input,'r').read()
    self.lines = [l.split('  ') for l in self.file.splitlines()]
    self.left_list = sorted([int(l[0]) for l in self.lines])
    self.right_list = sorted([int(l[1]) for l in self.lines])
    
  def p1(self):
    return  sum(abs(l - r) for l, r in zip(self.left_list, self.right_list))
  
  def p2(self):
    right_counts = Counter(self.right_list)
    return sum(num * right_counts[num] for num in self.left_list)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=False, default=1, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=False, default="False", type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False

  solution = DayOneSolution2024(test=test)
  result = solution.p1() if args.part == 1 else solution.p2()
  display_result(1, 1, result)