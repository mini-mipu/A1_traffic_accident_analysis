from apyori import apriori as apr
import pandas as pd

df = pd.read_csv('traffic_accident_data_v1.1.csv',encoding='utf-8')
data = df.values.tolist()
association_rules = apr(data, min_support=0.3, min_confidence=0.1, min_lift=2)
association_results = list(association_rules)


def write_result(association_results,minsup):
	if association_results != []: 
		wf = open(f'rule_result{str(minsup)}.txt','w',encoding='utf-8')
	count = 0
	for item in association_results:
		#[2][0][0]=>item base
		for item_num in range(0,len(item[2])):
			if item[2][item_num][0] == frozenset():
				continue
			else:
				pairBase= item[2][item_num][0]
				items = [x for x in pairBase]
				r="Rule: ("
				for x in range(0,len(items)):
					if x==0 :
						r=r+items[x]
					else:
						r=r+", "+items[x]

				r=r+") -> "
				#[2][0][1]=>item add
				pairAdd= item[2][item_num][1]
				items = [x for x in pairAdd]

				for x in range(0, len(items)):
					if x==0 :
						r=r+"("+items[x]
					else:
						r=r+", "+items[x]
						
				r=r+")"
				#print rule
				# print(r)
				wf.write(f'{r}\n')
				#[0] => all items in the rule
				# print("Length: "+str(len(item[0])))
				wf.write(f"Length: {str(len(item[0]))}\n")
				#[1] => support
				# print("Support: " + str(item[1]))
				wf.write(f"Support: {str(item[1])}\n")
				#[2][0][2] => confidence
				# print("Confidence: " + str(item[2][item_num][2]))
				wf.write(f"Confidence: {str(item[2][item_num][2])}\n")
				#[2][0][3] => lift
				# print("Lift: " + str(item[2][item_num][3]))
				wf.write(f"Lift: {str(item[2][item_num][3])}\n")
				# print("=====================================")
				wf.write("=====================================\n")
				count=count+1
				
	if association_results != []: wf.close()
	return count

write_result(association_results,0.08)