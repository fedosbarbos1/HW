import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, norm, ttest_rel


np.random.seed(0)
df_before = pd.DataFrame({ 
    "Pupil_Size_before":norm.rvs(size=10, loc=1, scale=1),
    "Weight_before":norm.rvs(size=10, loc=10, scale=40),
    "Height_before":norm.rvs(size=10, loc=50, scale=140),
    "VitaminD_after":norm.rvs(size=10, loc=7, scale=15),
    "BMI_before":norm.rvs(size=10, loc=12, scale=10),
    "IQ_before":norm.rvs(size=10, loc=50, scale=80),
    "Glucose_before":norm.rvs(size=10, loc=5, scale=3),
    "Hemaglobin_before":norm.rvs(size=10, loc=25, scale=50),
    "Ferritin_before":norm.rvs(size=10, loc=8, scale=20),
    "Cholesterol_before":norm.rvs(size=10, loc=1.5, scale=3),
     })


np.random.seed(1)
df_after = pd.DataFrame({ 
    "Pupil_Size_after":norm.rvs(size=10, loc=1, scale=1),
    "Weight_after":norm.rvs(size=10, loc=10, scale=40),
    "Height_after":norm.rvs(size=10, loc=50, scale=140),
    "VitaminD_after":norm.rvs(size=10, loc=7, scale=15),
    "BMI_after":norm.rvs(size=10, loc=12, scale=10),
    "IQ_after":norm.rvs(size=10, loc=50, scale=80),
    "Glucose_after":norm.rvs(size=10, loc=5, scale=3),
    "Hemaglobin_after":norm.rvs(size=10, loc=25, scale=50),
    "Ferritin_after":norm.rvs(size=10, loc=8, scale=20),
    "Cholesterol_after":norm.rvs(size=10, loc=1.5, scale=3),
     })


test_pupil_size_rel = ttest_rel(a = df_before.Pupil_Size_before, b = df_after.Pupil_Size_after)
test_weight_rel = ttest_rel(a = df_before.Weight_before, b = df_after.Weight_after)
test_height_rel = ttest_rel(a = df_before.Height_before, b = df_after.Height_after)
test_VitaminD_rel = ttest_rel(a = df_before.VitaminD_after, b = df_after.VitaminD_after)
test_BMI_rel = ttest_rel(a = df_before.BMI_before, b = df_after.BMI_after)
test_IQ_rel = ttest_rel(a = df_before.IQ_before, b = df_after.IQ_after)
test_glucose_rel = ttest_rel(a = df_before.Glucose_before, b = df_after.Glucose_after)
test_hemaglobin_rel = ttest_rel(a = df_before.Hemaglobin_before, b = df_after.Hemaglobin_after)
test_ferritin_rel = ttest_rel(a = df_before.Ferritin_before, b = df_after.Ferritin_after)
test_cholesterol_rel = ttest_rel(a = df_before.Cholesterol_before, b = df_after.Cholesterol_after)

print(test_pupil_size_rel)
print(test_weight_rel)
print(test_height_rel)
print(test_VitaminD_rel)
print(test_BMI_rel)
print(test_IQ_rel)
print(test_glucose_rel)
print(test_hemaglobin_rel)
print(test_ferritin_rel)
print(test_cholesterol_rel)


test_pupil_size_ind = ttest_ind(a = df_before.Pupil_Size_before, b = df_after.Pupil_Size_after)
test_weight_ind = ttest_ind(a = df_before.Weight_before, b = df_after.Weight_after)
test_height_ind = ttest_ind(a = df_before.Height_before, b = df_after.Height_after)
test_VitaminD_ind = ttest_ind(a = df_before.VitaminD_after, b = df_after.VitaminD_after)
test_BMI_ind = ttest_ind(a = df_before.BMI_before, b = df_after.BMI_after)
test_IQ_ind = ttest_ind(a = df_before.IQ_before, b = df_after.IQ_after)
test_glucose_ind = ttest_ind(a = df_before.Glucose_before, b = df_after.Glucose_after)
test_hemaglobin_ind = ttest_ind(a = df_before.Hemaglobin_before, b = df_after.Hemaglobin_after)
test_ferritin_ind = ttest_ind(a = df_before.Ferritin_before, b = df_after.Ferritin_after)
test_cholesterol_ind = ttest_ind(a = df_before.Cholesterol_before, b = df_after.Cholesterol_after)

print(test_pupil_size_ind)
print(test_weight_ind)
print(test_height_ind)
print(test_VitaminD_ind)
print(test_BMI_ind)
print(test_IQ_ind)
print(test_glucose_ind)
print(test_hemaglobin_ind)
print(test_ferritin_ind)
print(test_cholesterol_ind)

"""
pupil_size - размер зрачка (мм)
weight - вес (кг)
height - рост (см)
blood_pressure - давление (мм. рт. ст.)
BMI - индекс массы тела (кг/м²)
IQ - коэффициент интеллекта
glucose - уровень сахара в крови (ммоль/л)
hemaglobin - уровень гемаглобина в крови (г/л)
ferritin - уровень ферритина в крови (г/л)
cholesterol - уровень ферритина в крови (ммоль/л)
"""

#вопрос: не очень понятно, по какому принципу мы ставим значение в random.seed()