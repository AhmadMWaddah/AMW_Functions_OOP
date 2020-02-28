class MeanSquaredError:
    def __init__(self, actual_data, predicted_data):
        self.actual_data = actual_data
        self.predicted_data = predicted_data

    def mean_square_error(self):
        # Starter Counter.
        counter = 0
        # Combining BOth List With Zipping Function.
        data_combined = zip(self.actual_data, self.predicted_data)
        # Loop For Each cell in both data.
        for (each_actual, each_predicted) in data_combined:
            # Adding Results To Starter Counter.
            counter += (each_actual - each_predicted) ** 2
        return counter / len(self.actual_data)


class MeanForData:
    def __init__(self, data_values):
        self.data_values = data_values

    def data_mean(self):
        mean_for_data = sum(self.data_values) / len(self.data_values)
        return mean_for_data


class VarianceForData:
    def __init__(self, data_values, data_mean):
        self.data_values = data_values
        self.data_mean = data_mean

    def data_variance(self):
        starter_counter = 0
        for data_cells in self.data_values:
            starter_counter += (data_cells - self.data_mean) ** 2
        variance_for_data = starter_counter / len(self.data_mean)
        return variance_for_data


class CoVarianceForData:
    def __init__(self, features_values, labels_values, features_mean, labels_mean):
        self.features_values = features_values
        self.labels_values = labels_values
        self.features_mean = features_mean
        self.labels_mean = labels_mean

    def data_covariance(self):
        # Labels and Features Added and Multiplied.
        features_labels_sum_multiply = 0
        # Combine Both Features and Labels In One Object.
        feature_label_combined = zip(self.features_values, self.labels_values)
        for (features_values, labels_values) in feature_label_combined:
            features_labels_sum_multiply += (
                        (self.features_values - self.features_mean) * (self.labels_values - self.labels_mean))
        covariance_for_data = features_labels_sum_multiply / len(self.features_values)
        return covariance_for_data


class CoEfficientForData:
    def __init__(self, features_values, labels_values, features_mean, labels_mean):
        self.features_values = features_values
        self.labels_values = labels_values
        self.features_mean = features_mean
        self.labels_mean = labels_mean

    def data_coefficient(self):
        feat_mean = MeanForData(self.features_values)
        features_mean = feat_mean.data_mean()

        labe_mean = MeanForData(self.labels_values)
        labels_mean = labe_mean.data_mean()

        co_var_iance = CoVarianceForData(self.features_values, self.labels_values, self.features_mean, self.labels_mean)
        beta_one = co_var_iance.data_covariance()
        beta_zero = self.labels_values - (beta_one * self.features_mean)
        return beta_one, beta_zero


class SLRegression:
    def __init__(self, features_train, labels_train, features_test):
        self.features_train = features_train
        self.labels_train = labels_train
        self.features_test = features_test

    def simple_linear_regression(self):
        feats_mean, labe_means = MeanForData(self.features_train), MeanForData(self.labels_train)
        features_train_mean, labels_train_mean = feats_mean.data_mean(), labe_means.data_mean()

        all_coefficient = CoEfficientForData(self.features_train, self.labels_train, features_train_mean,
                                             labels_train_mean)
        beta_one_train, beta_zero_train = all_coefficient.data_coefficient()

        prediction_of_data = beta_one_train * self.features_test + beta_zero_train
        return prediction_of_data


class Evaluation:
    def __init__(self, trained_features, trained_labels, tested_features, tested_labels):
        self.trained_features = trained_features
        self.trained_labels = trained_labels
        self.tested_features = tested_features
        self.tested_labels = tested_labels

    def evaluate_model(self):
        predicts = SLRegression(self.trained_features, self.trained_labels, self.tested_features)
        prediction_data = predicts.simple_linear_regression()
        m_s_e = MeanSquaredError(self.tested_labels, prediction_data)
        final_evaluation = m_s_e.mean_square_error()
        return final_evaluation
