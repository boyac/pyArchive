# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-10-01 22:33:18
# @Last Modified by:   boyac
# @Last Modified time: 2016-10-02 00:56:00

class Diet():
	def __init__(self, kg, height, body_fat, bmi_goal, body_fat_goal):
		self.kg = kg
		self.height = height
		self.body_fat = body_fat
		self.bmi_goal = bmi_goal
		self.body_fat_goal = body_fat_goal


	def basal(self):
		self.basal = self.kg * 24
		return 'Your Basal Metabolism: {} kcal'.format(self.basal)


	def calo_share(self):
		unit = self.basal/6
		breakfast = unit * 3
		lunch = unit * 2
		dinner = unit * 1
		return 'Breakfast: {} kcal; Lunch: {} kcal; Dinner: {} kcal'.format(breakfast, lunch, dinner)


	def low_GI(self):
		'''
		5 key points of healthy diet:
		- high fiber
		- sufficient protein
		- good oil: 30-40g/daily
		- good carbs
		- sufficient water: 2L/daily

		Focus on low_GI diet, which GI is under < 60
		''' 

	def goal_bmi(self):
		'''
		Fat & Weight 
		BMI = 19-22
		Body_Fat = 22% (my current = 29%)
		'''
		bmi = self.kg / (self.height**2)
		ideal_bmi = 22 
		return 'Your Ideal BMI: {}; Your Current BMI: {}'.format(ideal_bmi, bmi)


	def goal_body_fat(self):

		self.body_fat = self.body_fat * self.kg
		self.ideal_fat = self.kg * self.body_fat_goal
		
		return 'Your Ideal Body Fat: {} Kgs; Your Current Body Fat: {} Kgs'.format(self.ideal_fat, self.body_fat)
		

	def plan(self, days):
		self.days = days
		self.to_lose = self.body_fat - self.ideal_fat
		monthly = self.to_lose / (days/30)
		ideal_weight = self.kg - self.to_lose
		to_lose = 'Your Ideal Weight: {} Kgs. You have to lose {} Kgs in {} days, {} Kgs monthly'.format(ideal_weight, self.to_lose, days, monthly)		
		return to_lose


	def decalo(self):
		decalo = self.to_lose * 7700 # calories to lose
		return 'You Should Lose {} kcal daily for {} days'.format(decalo/ self.days, self.days)



if __name__ == '__main__':
	d = Diet(57, 1.58, 0.29, 22, 0.22) # weight(kgs), height(m), body_fat(%), bmi_goal(integer), body_fat_goal(%)
	print d.basal()
	print d.calo_share()
	print d.goal_bmi()
	print d.goal_body_fat()
	print d.plan(60)
	print d.decalo()

	'''
	RESULT:
	Your Basal Metabolism: 1368 kcal
	Breakfast: 684 kcal; Lunch: 456 kcal; Dinner: 228 kcal
	Your Ideal BMI: 22; Your Current BMI: 22.8328793463
	Your Ideal Body Fat: 12.54 Kgs; Your Current Body Fat: 16.53 Kgs
	Your Ideal Weight: 53.01 Kgs. You have to lose 3.99 Kgs in 60 days, 1.995 Kgs monthly
	You Should Lose 512.05 kcal daily for 60 days
	'''
