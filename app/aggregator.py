import pandas as pd


def aggregator(csv):
    '''
    Arguments: Takes a single dataframe with prediction labels for each split of a song.
    Returns: Aggregates outputs and returns single output label for each song.
    '''
    flag = 0
    language_df = pd.DataFrame()
    label_df = pd.DataFrame()

    df = pd.read_csv(csv)
    # print(df)

    ### SEPARATING LANGUAGE AND LABEL FOR SEPARATE INFERENCING
    language_df = df.iloc[:, 1:-1]
    df = df.drop(['language'], axis=1)
    label_df= df.iloc[:, 1:]

    # print(label_df)
    # print(language_df)

    if flag == 0:
        label_df['song_name'] = label_df['song_name'].str[:-8]
        language_df['song_name'] = language_df['song_name'].str[:-8]
        flag = 1
    
    # label_df.iloc[0,:]

    label_df_groupby = label_df.groupby('song_name')
    language_df_groupby = language_df.groupby('song_name')

    from collections import Counter


    for name, group in label_df_groupby:
        label_list = []
        print( "##############")
    #     print(name)
        for each_label in group.label:
            label_list.append(each_label)
    #     print(lang)
        counts = dict(Counter(label_list))

        # print(name, counts)

        v, k = list(counts.values()), list(counts.keys())
        print(name)
        print(k[v.index(max(v))])

        duplicates = {key:value for key, value in counts.items() if value > 1}
        # print(name, duplicates)

    for name, group in language_df_groupby:
        language_list = []
        print( "##############")
    #     print(name)
        for each_language in group.language:
            language_list.append(each_language)
    #     print(lang)
        counts = dict(Counter(language_list))
        # print(language_list)
        # print(name)
        # print(counts)

        v, k = list(counts.values()), list(counts.keys())

        print(v, k)
        print(counts)
        print(name)
        if max(v) >= len(language_list)//2: ############ 50% confidence threshold
            print(k[v.index(max(v))])
        else:
            print("Language not confident")
        # duplicates = {key:value for key, value in counts.items() if value > 1}
        # print(name, duplicates)


    # print(df)
    # label_aggregator = df.iloc[:, :-1]
    # looper = label_aggregator
    # print(looper)
    # looper = df.groupby('song_name')
    # print(looper)
    # # df.groupby('song_name').agg([np.mean])

# def custom_grouping(['label', 'language'], df_groupby):
#     for name, group in df_groupby:
#         labeller_list = []








# aggregator("prediction_labels_splits.csv")