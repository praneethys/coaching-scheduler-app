import moment from "moment-timezone";

export const formatDateTime = (inputDate?: Date | string): string => {
  const formattedDate = moment(inputDate).format("MMM DD, YYYY hh:mm A");
  return formattedDate;
};

export const getTimezone = (inputDate: Date | string): string => {
  const zoneName = moment.tz.guess();
  const zoneAbbr = moment.tz.zone(zoneName)?.abbr(moment(inputDate).unix());
  console.log(
    `Timezone for given inputDate: ${moment(inputDate).format(
      "YYYY/MM/DD hh:mm:ss"
    )} is ${zoneAbbr}`
  );
  return zoneAbbr || "";
};
