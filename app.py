import pandas as pd
import math
import csv
import random
from random import shuffle
import streamlit as st


def generate_sentence(): 
    vowels = ["a", "e", "i", "o", "u", "y", "w"]

    df = pd.read_csv('Welsh flashcards.csv', sep=";")

    #print(df.head())
    words = df['word'].tolist()
    #print(words)

    adv_index = df.index[df['type'] == 'adverb'].tolist()
    #print(adv_index)

    adv_words = []
    for index in adv_index:
        word = words[index]
        adv_words.append(word)
        #print(word)

    #print(adv_words)
    #print(adv_words[1])

    def pick_words(list_index):
        newlist = []
        for index in list_index:
            word = words[index]
            newlist.append(word)
        return newlist

    verbnoun_index = df.index[df['type'] == 'verbnoun'].tolist()
    #print(verbnoun_index)
    verbnoun_list = pick_words(verbnoun_index)
    #print(verbnoun_list)

    def soft_mutation(word):
        word = str(word)
        if word[0] == "d":
            word = word.replace("d", "dd")
        if word[0] == "t":
            word = word.replace("t", "d")
        if word[0] == "g":
            word = word.replace("g", "")
        if word[0] == "c":
            word = word.replace("c", "g")
        if word[0] == "b":
            if word != "braf":
                word = word.replace("b", "f")
        if word[0:2] == "rh":
            word = word.replace("rh", "r")
        if word[0] == "m":
            word = word.replace("m", "f")
        if word[0] == "p":
            word = word.replace("p", "b")
        if word[0:2] == "ll":
            word = word.replace("ll", "l")
        return word


    adv_q1_index = df.index[df['type'] == 'adverb'].tolist()
    #print(adv_q1_index)
    adv_q2_index = df.index[df['q'] == 'q'].tolist()
    #print(adv_q2_index)
    adv_q_index = []
    for index in adv_q2_index:
        if index in adv_q1_index:
            adv_q_index.append(index)

    #print(adv_q_index)

    bod_q1_index = df.index[df['type'] == 'v_bod'].tolist()
    #print(bod_q1_index)
    bod_q2_index = df.index[df['q'] == 'q'].tolist()
    #print(bod_q2_index)
    bod_q_index = []
    for index in bod_q2_index:
        if index in bod_q1_index:
            bod_q_index.append(index)

    #print(bod_q_index)

    vndyn1_index = df.index[df['type'] == 'verbnoun'].tolist()
    #print(vndyn1_index)
    vndyn2_index = df.index[df['stat_dyn'] == 'dyn'].tolist()
    #print(vndyn2_index)
    vndyn_index = []
    for index in vndyn1_index:
        if index in vndyn2_index:
            vndyn_index.append(index)

    #print(vndyn_index)

    adv_fut1_index = df.index[df['type'] == 'adverb'].tolist()
    #print(adv_fut1_index)
    adv_fut2_index = df.index[df['tense'] == 'future'].tolist()
    #print(adv_fut2_index)
    adv_fut_index = []
    for index in adv_fut1_index:
        if index in adv_fut2_index:
            adv_fut_index.append(index)

    #print(adv_fut_index)


    gwneudpq1_index = df.index[df['type'] == 'v_gwneud'].tolist()
    #print(gwneudpq1_index)
    gwneudpq2_index = df.index[df['q'] == 'q'].tolist()
    #print(gwneudpq2_index)
    gwneudpq3_index = df.index[df['tense'] == 'past'].tolist()
    #print(gwneudpq3_index)

    gwneudpq_indexer = []
    for index in gwneudpq2_index:
        if index in gwneudpq1_index:
            gwneudpq_indexer.append(index)
    gwneudpq_index = []
    for index in gwneudpq3_index:
        if index in gwneudpq_indexer:
            gwneudpq_index.append(index)

    #print(gwneudpq_index)


    adv_q1_index = df.index[df['type'] == 'adverb'].tolist()
    #print(adv_q1_index)
    adv_q2_index = df.index[df['tense'] == 'past'].tolist()
    #print(adv_q2_index)
    adv_past_index = []
    for index in adv_q2_index:
        if index in adv_q1_index:
            adv_past_index.append(index)

    #print(adv_past_index)


    bod3s1_index = df.index[df['type'] == 'v_bod'].tolist()
    #print(bod3s1_index)
    bod3s2_index = df.index[df['sg_pl'] == 'sg'].tolist()
    #print(bod3s2_index)
    bod3s3_index = df.index[df['number'] == 3].tolist()
    #print(bod3s3_index)
    bod3s4_index = df.index[df['q'] != 'q'].tolist()
    #print(bod3s4_index)

    bod3s_indexer = []
    for index in bod3s2_index:
        if index in bod3s1_index:
            bod3s_indexer.append(index)
    bod3s_indexes = []
    for index in bod3s3_index:
        if index in bod3s_indexer:
            bod3s_indexes.append(index)
    #print(bod3s_indexes)
    bod3s_index = []
    for index in bod3s4_index:
        if index in bod3s_indexes:
            bod3s_index.append(index)
    #print(bod3s_index)



    qbod3s1_index = df.index[df['type'] == 'v_bod'].tolist()
    #print(qbod3s1_index)
    qbod3s2_index = df.index[df['sg_pl'] == 'sg'].tolist()
    #print(qbod3s2_index)
    qbod3s3_index = df.index[df['number'] == 3].tolist()
    #print(qbod3s3_index)
    qbod3s4_index = df.index[df['q'] == 'q'].tolist()
    #print(qbod3s4_index)

    qbod3s_indexer = []
    for index in qbod3s2_index:
        if index in qbod3s1_index:
            qbod3s_indexer.append(index)
    qbod3s_indexes = []
    for index in qbod3s3_index:
        if index in qbod3s_indexer:
            qbod3s_indexes.append(index)
    #print(qbod3s_indexes)
    bod3sq_index = []
    for index in qbod3s4_index:
        if index in qbod3s_indexes:
            bod3sq_index.append(index)
    #print(bod3sq_index)


    adj_w1_index = df.index[df['type'] == 'adj'].tolist()
    #print(adj_w1_index)
    adj_w2_index = df.index[df['cat'] == 'weather'].tolist()
    #print(adj_w2_index)
    adj_weather_index = []
    for index in adj_w2_index:
        if index in adj_w1_index:
            adj_weather_index.append(index)

    #print(adj_weather_index)


    gaf_q1_index = df.index[df['type'] == 'v_gaf'].tolist()
    #print(gaf_q1_index)
    gaf_q2_index = df.index[df['q'] == 'q'].tolist()
    #print(gaf_q2_index)
    gaf_q_index = []
    for index in gaf_q2_index:
        if index in gaf_q1_index:
            gaf_q_index.append(index)

    #print(gaf_q_index)


    mynd_past1_index = df.index[df['type'] == 'v_mynd'].tolist()
    #print(mynd_past1_index)
    mynd_past2_index = df.index[df['tense'] == 'past'].tolist()
    #print(mynd_past2_index)
    mynd_past_index = []
    for index in mynd_past2_index:
        if index in mynd_past1_index:
            mynd_past_index.append(index)

    #print(mynd_past_index)


    nounplace1_index = df.index[df['type'] == 'noun'].tolist()
    #print(nounplace1_index)
    nounplace2_index = df.index[df['cat'] == 'place'].tolist()
    #print(nounplace2_index)
    nounplace_index = []
    for index in nounplace2_index:
        if index in nounplace1_index:
            nounplace_index.append(index)

    #print(nounplace_index)


    bodpresent1_index = df.index[df['type'] == 'v_bod'].tolist()
    #print(bodpresent1_index)
    bodpresent2_index = df.index[df['tense'] != 'past'].tolist()
    #print(bodpresent2_index)
    bodpresent3_index = df.index[df['q'] != 'q'].tolist()
    #print(bodpresent3_index)

    bodpresent_indexes = []
    for index in bodpresent2_index:
        if index in bodpresent1_index:
            bodpresent_indexes.append(index)
    bodpresent_index = []
    for index in bodpresent3_index:
        if index in bodpresent_indexes:
            bodpresent_index.append(index)
    #print(bodpresent_index)


    verbnoun_index = df.index[df['type'] == 'verbnoun'].tolist()
    adj_index = df.index[df['type'] == 'adj'].tolist()
    noun_index = df.index[df['type'] == 'noun'].tolist()
    #print(noun_index)


    adv_q_list = pick_words(adv_q_index)
    bod_q_list = pick_words(bod_q_index)
    bodpresent_list = pick_words(bodpresent_index)
    vndyn_list = pick_words(vndyn_index)
    adv_fut_list = pick_words(adv_fut_index)
    gwneudpq_list = pick_words(gwneudpq_index)
    adv_past_list = pick_words(adv_past_index)
    bod3s_list = pick_words(bod3s_index)
    bod3sq_list = pick_words(bod3sq_index)
    adj_weather_list = pick_words(adj_weather_index)
    gaf_q_list = pick_words(gaf_q_index)
    mynd_past_list = pick_words(mynd_past_index)
    nounplace_list = pick_words(nounplace_index)
    verbnoun_list = pick_words(verbnoun_index)
    adj_list = pick_words(adj_index)
    nounsg_list = pick_words(noun_index)
        
    plurals = df['noun_pl'].tolist()
    plural_list = []
    for index in noun_index:
        word = plurals[index]
        if word != "n":
            plural_list.append(word)
    #print(plural_list)

    nounfull_list = nounsg_list + plural_list
    #print(nounfull_list)



    def function_1():
        aa = random.choice(adv_q_list).capitalize()
        ab = random.choice(bod_q_list)
        ac = random.choice(verbnoun_list)
        beth_bod_2ndp = ["wyt ti", "dych chi"]
        structure_1 = aa + " " + ab  + ((("'n " if ab[-1] in vowels else " yn ") + ac) if ac in vndyn_list else " " + (soft_mutation(ac) if aa == "Beth" and ab in beth_bod_2ndp else ac)) +"?"
        return structure_1

    def function_2():
        structure_2 = random.choice(bod_q_list).capitalize() + " eisiau " + random.choice(verbnoun_list) + "?"
        return structure_2

    def function_3():
        ca = random.choice(bodpresent_list)
        structure_3 = "Ble " + ca + ("'n " if ca[-1] in vowels else " yn ") + random.choice(vndyn_list) + " " + random.choice(adv_fut_list) + "?"
        return structure_3


    def function_4():
        structure_4 = random.choice(gwneudpq_list).capitalize() + " " + soft_mutation(random.choice(verbnoun_list)) + " " + random.choice(adv_past_list) + "?"
        return structure_4



    def function_5():
        structure_5 = "Beth " + random.choice(gwneudpq_list) + " " + random.choice(adv_past_list) + "?"
        return structure_5


    def function_6():
        fa = random.choice(bod_q_list).capitalize()
        fb = [soft_mutation(item) for item in adj_list]
        fc = fb + verbnoun_list
        fd = random.choice(fc)
        structure_6 = fa + ((("'n " if fa[-1] in vowels else " yn ") + fd) if fd in (vndyn_list or adj_list) else " " + fd) + "?"
        return structure_6


    def function_7():
        ga = nounfull_list + verbnoun_list
        structure_7 = random.choice(gaf_q_list).capitalize() + " " + soft_mutation(random.choice(ga)) +"?"
        return structure_7


    def function_8():
        structure_8 = random.choice(adv_q_list).capitalize() + " " + random.choice(mynd_past_list) + " " + random.choice(adv_past_list) + "?"
        return structure_8

    def function_9():
        structure_9 = random.choice(mynd_past_list).capitalize() + " i " + soft_mutation(random.choice(verbnoun_list)) + " " + random.choice(adv_past_list) + "?"
        return structure_9


    def function_10():
        structure_10 = random.choice(mynd_past_list).capitalize() + " i " + soft_mutation(random.choice(nounplace_list)) + "?"
        return structure_10

    def pick_sentence():
        function_options = [function_1(), function_2(), function_3(), function_4(), function_5(), function_6(), function_7(), function_8(), function_9(), function_10()]
        return random.choice(function_options)
    #pick_sentence()



    print(pick_sentence())
    return pick_sentence()





st.title("Dysgu Cymraeg: sentence practice")
st.write("Mynediad 1, unedau 1-10")

sentence = generate_sentence()
st.info(f"{sentence}")


if st.button("Generate Another"):
    st.rerun()