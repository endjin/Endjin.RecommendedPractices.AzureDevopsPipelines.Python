class DataframeOperations:
    @staticmethod
    def count_females(df):
        gender_counts = df["Gender"].value_counts()
        return gender_counts['Female']