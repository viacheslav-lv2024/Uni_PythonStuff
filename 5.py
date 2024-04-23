lines_on_page, num_of_line = map(int, input().split())
ans_page = num_of_line // lines_on_page + 1
ans_line = num_of_line - (num_of_line // lines_on_page) * lines_on_page
print(ans_page, ans_line)